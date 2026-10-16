"""Reviewed, source-backed device facts. No generated prices or invented compatibility."""
import json,re
from urllib.parse import urlparse
from public_fetch import _read,_write,ROOT,fetch_public

FEATURES={
 'display':('屏幕','display','ディスプレイ'),'touch':('触摸输入','touch input','タッチ入力'),'keyboard':('键盘','keyboard','キーボード'),'audio':('音频输入输出','audio I/O','オーディオ入出力'),'microphone':('麦克风','microphone','マイク'),'speaker':('扬声器','speaker','スピーカー'),'imu':('运动传感器','motion sensor','モーションセンサー'),'battery':('电池供电','battery power','バッテリー電源'),'epaper':('电子纸屏幕','e-paper display','電子ペーパーディスプレイ'),'usb':('USB 接口','USB connection','USB接続'),'gpio':('GPIO 扩展','GPIO expansion','GPIO拡張'),'ethernet':('以太网','Ethernet','Ethernet'),'camera':('摄像头','camera','カメラ'),'lora':('LoRa 无线模块','LoRa radio','LoRa無線'),'gps':('定位模块','GNSS receiver','GNSS受信機'),'encoder':('旋转编码器','rotary encoder','ロータリーエンコーダー'),'rfid':('RFID 读取','RFID reader','RFIDリーダー'),'subghz':('Sub-GHz 无线模块','sub-GHz radio','Sub-GHz無線'),'sd':('存储卡接口','memory-card slot','メモリーカードスロット'),'rs485':('RS-485 接口','RS-485 interface','RS-485インターフェース'),'rgb':('RGB 指示灯','RGB indicator','RGBインジケーター')}
# Each row is a manual selection of conservative hardware facts after reviewing the linked primary page.
PROFILES=[
 ('m5stack-atom','ATOM Lite',['gpio','rgb'],'迷你自动化控制板','compact automation board','小型の自動化ボード','m5stack-atom-lite'),
 ('m5stack-atoms3','AtomS3',['display','imu','gpio'],'迷你带屏开发设备','compact display device','小型の画面付きデバイス',None),
 ('m5stack-core-esp32','BASIC',['display','speaker','gpio'],'可堆叠的模块化控制器','stackable modular controller','積み重ね式のモジュール型コントローラー','m5stack-basic'),
 ('m5stack-core2','Core2',['display','touch','audio','imu'],'触控物联网终端','touchscreen IoT terminal','タッチ式のIoT端末',None),
 ('m5stack-coreink','CoreInk',['epaper','battery','gpio'],'低功耗信息显示设备','low-power information display','低消費電力の情報表示デバイス',None),
 ('m5stack-cores3','CoreS3',['display','touch','camera','audio'],'集成多种交互外设的控制器','controller with integrated interactive peripherals','複数の操作機能を搭載したコントローラー',None),
 ('m5stack-dial','Dial V1.1',['display','touch','encoder','rfid'],'旋钮式控制终端','rotary control terminal','ダイヤル式の操作端末',None),
 ('m5stack-fire','FIRE',['display','audio','imu'],'模块化传感与显示控制器','modular sensing and display controller','モジュール型のセンサー・表示コントローラー',None),
 ('m5stack-station','Station-485',['display','rs485','gpio'],'盒式工业与桌面控制器','enclosed industrial and desktop controller','ケース入りの産業・デスク用コントローラー','m5stack-station-485'),
 ('m5stack-tab5','Tab5',['display','touch','camera','rs485'],'平板形态交互终端','tablet-style interaction terminal','タブレット型の操作端末',None),
 ('m5stack-timer-cam','Timer Camera',['camera','battery'],'定时图像采集开发设备','timer-based camera development device','タイマー撮影用の開発デバイス',None),
 ('m5stick-c','M5StickC',['display','imu','battery'],'便携式传感开发设备','portable sensing development device','携帯型のセンサー開発デバイス','m5stack-stickc'),
 ('lilygo-t-beam-supreme','T-Beam Supreme',['lora','gps'],'无线定位与遥测开发板','wireless positioning and telemetry board','無線測位・テレメトリー用ボード',None),
 ('lilygo-t-beam','T-Beam',['lora','gps'],'无线定位开发板','wireless positioning board','無線測位用ボード',None),
 ('lilygo-t-deck-plus','T-Deck Plus',['display','keyboard','gps','battery','lora'],'键盘式便携终端','portable keyboard terminal','キーボード付き携帯端末',None),
 ('lilygo-t-deck','T-Deck',['display','keyboard','audio'],'可编程掌上终端','programmable handheld terminal','プログラム可能な携帯端末',None),
 ('lilygo-t-display-s3','T-Display S3',['display','gpio'],'彩色屏幕开发板','color-display development board','カラー画面付き開発ボード',None),
 ('lilygo-t-dongle-s3','T-Dongle S3',['display','usb'],'USB 插棒式开发设备','USB dongle development device','USBドングル型の開発デバイス',None),
 ('lilygo-t-embed-cc1101','T-Embed CC1101',['display','encoder','subghz'],'带旋钮的无线工具开发设备','wireless tool development device with a dial','ダイヤル付き無線ツール開発デバイス',None),
 ('lilygo-t-embed','T-Embed',['display','encoder','audio'],'可嵌入式交互面板','embeddable interactive panel','組み込み型の操作パネル',None),
 ('lilygo-t-eth-lite','T-ETH-Lite ESP32',['ethernet','sd'],'有线联网开发板','wired-network development board','有線ネットワーク開発ボード',None),
 ('lilygo-t-watch-s3','T-Watch S3',['display','touch','lora'],'可编程手表开发平台','programmable watch development platform','プログラム可能な腕時計開発プラットフォーム',None),
 ('lilygo-t3s3-v1-0','T3 S3',['display','lora'],'带显示屏的无线电开发板','radio development board with a display','画面付き無線開発ボード',None),
 ('lilygo-t4-s3','T4 S3',['display','sd'],'AMOLED 信息显示开发板','AMOLED information-display board','AMOLED情報表示用ボード',None),
 ('lilygo-t5-4-7-epaper-v2-3','T5 4.7 E-Paper V2.3',['epaper','sd'],'电子纸交互面板','interactive e-paper panel','電子ペーパー操作パネル',None),
 ('lilygo-ttgo-t-display-1-14','T-Display 1.14',['display','gpio'],'小型显示开发板','small display development board','小型の画面付き開発ボード',None),
 ('ttgo-lora32','LoRa32 OLED V1.6.1',['display','lora'],'长距离无线通信开发板','long-range wireless development board','長距離無線通信用ボード','lilygo-lora32-oled'),
 ('twatch','T-Watch 2020',['display','touch','imu','battery'],'可编程穿戴设备','programmable wearable device','プログラム可能なウェアラブルデバイス','lilygo-t-watch-2020'),
 ('esp32-c3-zero','ESP32-C3-Zero',['usb','gpio'],'紧凑型通用开发板','compact general-purpose development board','小型の汎用開発ボード','waveshare-esp32-c3-zero'),
 ('esp32-c6-zero-mini','ESP32-C6-Zero',['usb','gpio'],'紧凑型联网开发板','compact connected-device development board','小型のネットワーク開発ボード','waveshare-esp32-c6-zero'),
 ('esp32-s3-zero','ESP32-S3-Zero',['usb','gpio'],'紧凑型通用开发板','compact general-purpose development board','小型の汎用開発ボード','waveshare-esp32-s3-zero'),
 ('waveshare-esp32-s3-epaper-1-54g','ESP32-S3-ePaper-1.54G',['epaper','gpio'],'小型电子纸信息面板','small e-paper information panel','小型電子ペーパー情報パネル',None),
 ('waveshare-esp32-s3-touch-lcd-7b','ESP32-S3-Touch-LCD-7B',['display','touch'],'大屏触控人机界面开发设备','large touchscreen HMI development device','大型タッチ画面のHMI開発デバイス',None),
 ('xiao-esp32c3','XIAO ESP32C3',['usb','gpio'],'微型无线开发板','miniature wireless development board','超小型の無線開発ボード','seeed-xiao-esp32c3'),
 ('xiao-esp32c5','XIAO ESP32C5',['usb','gpio'],'微型双频 Wi-Fi 开发板','miniature dual-band Wi-Fi board','超小型のデュアルバンドWi-Fiボード','seeed-xiao-esp32c5'),
 ('xiao-esp32c6','XIAO ESP32C6',['usb','gpio'],'微型多协议无线开发板','miniature multiprotocol wireless board','超小型のマルチプロトコル無線ボード','seeed-xiao-esp32c6'),
 ('xiao-esp32s3-plus','XIAO ESP32S3 Plus',['usb','gpio'],'扩展接口更多的微型开发板','miniature development board with additional I/O','拡張端子を増やした超小型開発ボード','seeed-xiao-esp32s3-plus'),
 ('xiao-esp32s3-sense','XIAO ESP32S3 Sense',['camera','microphone','sd'],'面向图像和声音的微型开发设备','miniature image and audio development device','画像・音声向けの超小型開発デバイス','seeed-xiao-esp32s3-sense'),
 ('xiao-esp32s3','XIAO ESP32S3',['usb','gpio'],'微型通用开发板','miniature general-purpose development board','超小型の汎用開発ボード','seeed-xiao-esp32s3'),
 ('esp32-c3-devkitc-02','ESP32-C3-DevKitC-02',['usb','gpio'],'官方通用开发板','official general-purpose development board','公式の汎用開発ボード','espressif-esp32-c3-devkitc-02'),
]

def chip_name(value):return re.sub(r'^ESP32([SC H P])',r'ESP32-\1',value.replace(' ',''))
def summary(brand,chip,features,purposes):
    labels=[[FEATURES[f][i] for f in features] for i in range(3)]
    return {'zh':f'{brand} 的{purposes[0]}，采用 {chip}，配有'+'、'.join(labels[0])+'。','en':f'{brand} {purposes[1]} based on {chip}, with '+', '.join(labels[1])+'.','ja':f'{chip}を搭載した{brand}の{purposes[2]}。'+'、'.join(labels[2])+'を備えています。'}

def main():
    candidates=_read(ROOT/'data/collection/device-candidates.json',{})
    by_id={item['id']:item for item in candidates.values()}
    output=[]
    names={'m5stack':'M5Stack','lilygo':'LILYGO','waveshare':'Waveshare','seeed-studio':'Seeed Studio','espressif':'Espressif'}
    for source_id,name,features,zh,en,ja,id_override in PROFILES:
        candidate=by_id[source_id];d=candidate['details']
        if d.get('primaryStatus')!='checked' or not d.get('primaryTitle'):continue
        id=id_override or source_id
        maker=d['manufacturer']['id'];brand=names.get(maker,d['manufacturer']['name']);chip=chip_name(d['chip'])
        data={'id':id,'name':name,'manufacturer':{'id':maker,'name':brand},'chip':chip,'summary':summary(brand,chip,features,[zh,en,ja]),'officialUrl':d['officialUrl'],'aliases':[d['name']],'features':features,'sources':[{'url':candidate['sourceUrl'],'checkedAt':d['sourceCheckedAt']},{'url':d['officialUrl'],'checkedAt':d['primaryCheckedAt']}]}
        output.append({'kind':'device','data':data,'note':'Source-backed hardware facts. Exact revisions and optional radio modules follow the manufacturer documentation; project compatibility is recorded separately.'})
        candidate['contentId']=id
    extras=_read(ROOT/'data/collection/additional-device-candidates.json',{})
    types={
      'm5stack-stopwatch':('圆形触控穿戴开发设备','round touchscreen wearable development device','円形タッチ画面のウェアラブル開発デバイス'),
      'm5stack-sticks3':('便携式语音与传感开发设备','portable voice and sensing development device','携帯型の音声・センサー開発デバイス'),
      'm5stack-stickc-plus2':('便携式传感开发设备','portable sensing development device','携帯型のセンサー開発デバイス'),
      'm5stack-cardputer-adv':('带键盘的掌上开发终端','handheld keyboard development terminal','キーボード付き携帯開発端末'),
      'm5stack-papers3':('电子纸触控开发终端','touchscreen e-paper development terminal','タッチ式電子ペーパー開発端末'),
      'waveshare-esp32-s3-touch-amoled-1-8':('AMOLED 桌面与便携交互开发板','AMOLED desktop and portable interaction board','AMOLED画面のデスク・携帯操作ボード'),
      'waveshare-esp32-s3-touch-amoled-2-06':('AMOLED 交互开发板','AMOLED interaction development board','AMOLED画面の操作開発ボード'),
    }
    for id,record in extras.items():
        if not record.get('primaryCheckedAt'):continue
        data={key:record[key] for key in ['id','name','manufacturer','chip','officialUrl','features']}
        data['aliases']=[data['manufacturer']['name']+' '+data['name']]
        data['summary']=summary(data['manufacturer']['name'],data['chip'],data['features'],types[id])
        data['sources']=[{'url':record['discoveredVia']},{'url':data['officialUrl'],'checkedAt':record['primaryCheckedAt']}]
        output.append({'kind':'device','data':data,'note':'Do not infer firmware compatibility solely from the ESP32 chip family. Hardware revisions and peripherals must match the upstream project.'})
    _write(ROOT/'data/collection/reviewed-devices.json',output)
    _write(ROOT/'data/collection/device-candidates.json',candidates)
    print('Reviewed devices prepared:',len(output))

if __name__=='__main__':main()

import { useEffect, useRef, useState } from 'react'

/** Uses the original image host; failed requests fall back to the device name. */
export function DeviceImage({ src, name, maker, eager = false }: { src?: string; name: string; maker: string; eager?: boolean }) {
  const [failed, setFailed] = useState<string>()
  const imageRef = useRef<HTMLImageElement>(null)
  useEffect(() => {
    const image = imageRef.current
    if (src && image?.complete && image.naturalWidth === 0) setFailed(src)
  }, [src])
  return src && failed !== src
    ? <img ref={imageRef} src={src} alt={name} loading={eager ? 'eager' : 'lazy'} onError={() => setFailed(src)} />
    : <span className="name-cover"><small>{maker}</small><strong>{name}</strong></span>
}

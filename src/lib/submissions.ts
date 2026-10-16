export const repositoryUrl = 'https://github.com/hr98w/esp32.sh'
export const projectSubmissionLabel = 'submission:project'
export const projectSubmissionTemplate = 'submit-project.yml'
export function projectSubmissionUrl() {
  return `${repositoryUrl}/issues/new?template=${projectSubmissionTemplate}`
}

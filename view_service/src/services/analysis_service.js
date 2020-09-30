import axios from 'axios'

/**
 * A access layer to the analysis service.
 *
 * @constructor
 */
export default class AnalysisService {
  /**
   * {AnalysisService} constructor.
   */
  constructor () {
    this.client = axios.create({ baseURL: `${process.env.VUE_APP_ANALYZER_URL}/api/analyze/` })
  }

  /**
   * Performs the analyzis.
   *
   * @param {object} data - The parameters to the analysis.
   * @param {function} successCallBack.
   * @param {function} errorCallback.
   * @param {function} finallyCallback.
   */
  analyze (data, successCallBack, errorCallback, finallyCallback) {
    this.client.post('', data)
      .then(successCallBack)
      .catch(errorCallback)
      .then(finallyCallback)
  }
}

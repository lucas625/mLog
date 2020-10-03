<template>
  <v-container
    class="fill-height"
    fluid
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col
        cols="10"
        md="8"
      >
        <v-card
          class="elevation-12"
          :loading="isAnalysisRunning"
        >
          <v-toolbar
            color="primary"
            dark
            flat
          >
            <v-toolbar-title>Analyze the Sales</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form ref="analysisForm">
              <v-row>
                <v-col
                  cols="12"
                  lg="6"
                  align="center"
                >
                  <v-subheader class="pl-0">
                    Start Date
                  </v-subheader>
                  <v-date-picker v-model="startDate" />
                </v-col>
                <v-col
                  cols="12"
                  lg="6"
                  align="center"
                >
                  <v-subheader class="pl-0">
                    End Date
                  </v-subheader>
                  <v-date-picker
                    v-model="endDate"
                    :min=startDate
                  />
                </v-col>
              </v-row>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-row>
              <v-col align="center">
                <v-btn
                  color="primary"
                  @click="submit"
                >
                  <v-icon left>
                    mdi-download
                  </v-icon>
                  Download CSV
                </v-btn>
              </v-col>
            </v-row>   
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import AnalysisService from '@/services/analysis_service'

const analysisService = new AnalysisService()

/**
 * Performs the submit.
 * @private
 */
function _submit () {
  if (this.$refs.analysisForm.validate()) {
    
    this.isAnalysisRunning = true
    const analysisParameters = {
      start_date: this.startDate,
      end_date: this.endDate
    }

    const successCallBack = (response) => {
      let blob = new Blob([response.data], { type: 'text/csv' })
      let link = document.createElement('a')
      link.href = window.URL.createObjectURL(blob)
      link.download = 'analysis.csv'
      link.click()
    }

    const errorCallBack = (error) => {
      alert('Failed to download')
    }

    const finallyCallBack = () => {
      this.isAnalysisRunning = false
    }

    analysisService.analyze(analysisParameters, successCallBack, errorCallBack, finallyCallBack)
  }
}

export default {
  name: 'AnalysisView',
  data: function () {
    return {
      /**
       * The lower date limit to analyze.
       */
      startDate: new Date().toISOString().split('T')[0],
      /**
       * The upper date limit to analyze.
       */
      endDate: new Date().toISOString().split('T')[0],
      /**
       * Flag to show if the analysis is running.
       */
      isAnalysisRunning: false
    }
  },
  computed: {
    /**
     * Rule that verifies if the end date is bigger than the lower date.
     */
    endDateRule: function () {
      return Boolean(this.endDate >= this.startDate) || 'The end date must be bigger than the lower date.'
    }
  },
  methods: {
    submit: _submit,

  }
}
</script>

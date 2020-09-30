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
        sm="8"
        md="6"
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
              <v-text-field
                v-model="days"
                :rules="days_rules"
                hint="Days before today to be analyzed."
                label="Days"
                type="number"
                prepend-icon="mdi-calendar-range"
              />
              </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              @click="submit"
            >
              <v-icon left>
                mdi-download
              </v-icon>
              Download CSV
            </v-btn>
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
    console.log(process.env.VUE_APP_ANALYZER_URL)
    this.isAnalysisRunning = true
    const analysisParameters = {
      // days: this.days
    }

    const successCallBack = (response) => {
      const blob = new Blob([response.data], { type: 'text/csv' })
      const url = window.URL.createObjectURL(blob)
      window.open(url)
    }

    const errorCallBack = (error) => {
      console.log(error)
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
       * Days before today to analyze the logs.
       */
      days: null,
      /**
       * Rules for the days field.
       */
      days_rules: [
        (value) => (Boolean(value) && value.length > 0) || 'This field is required',
        (value) => value > 0 || 'We need at least 1 day to perform the analysis.'
      ],
      /**
       * Flag to show if the analysis is running.
       */
      isAnalysisRunning: false
    }
  },
  methods: {
    submit: _submit,

  }
}
</script>

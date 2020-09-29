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
          cols="12"
          sm="8"
          md="4"
      >
        <v-card class="elevation-12">
          <v-toolbar
              color="primary"
              dark
              flat
          >
            <v-toolbar-title>Analyze the Sales</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                  v-model="days"
                  :rules="days_rules"
                  label="Days"
                  type="number"
                  prepend-icon="mdi-account"
              />
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary">
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

import AnalysisService from '@/services/AnalysisService'

const analysisService = new AnalysisService()

export default {
  name: 'RegisterView',
  data: function () {
    return {
      /**
       * Days before today to analyze the logs.
       */
      days: 14,
      /**
       * Rules for the days field.
       */
      days_rules: [
        (value) => (Boolean(value) && value.length > 0) || 'This field is required',
        (value) => value > 0 || 'We need at least 1 day to perform the analysis.'
      ]
    }
  }
}
</script>

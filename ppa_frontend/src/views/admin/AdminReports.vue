<template>
  <div class="admin-reports">
    <h3 class="mb-4">Placement Reports & Statistics</h3>
    
    <div class="alert alert-info mt-3 shadow-sm">
      <i class="bi bi-info-circle-fill me-2"></i>
      <strong>Note:</strong> Detailed monthly reports are automatically generated on the 1st of every month.
    </div>

    <div class="card mt-4 shadow-sm border-0">
      <div class="card-header bg-dark text-white">System Overview (Live Data)</div>
      <div class="card-body">
        <ul class="list-group list-group-flush">
          <li class="list-group-item d-flex justify-content-between align-items-center">
            Total Students Registered
            <span class="badge bg-primary rounded-pill">{{ stats.total_students }}</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center">
            Total Companies Registered
            <span class="badge bg-primary rounded-pill">{{ stats.total_companies }}</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center">
            Total Placement Drives
            <span class="badge bg-primary rounded-pill">{{ stats.total_placement_drives }}</span>
          </li>
        </ul>
      </div>
    </div>

    <div class="card mt-4 shadow-sm border-0">
      <div class="card-header bg-secondary text-white d-flex justify-content-between align-items-center">
        <span>Monthly Activity Reports</span>
        <button @click="triggerReport" class="btn btn-sm btn-warning text-dark" :disabled="generating">
          {{ generating ? 'Generating...' : 'Generate Report Now' }}
        </button>
      </div>
      <div class="card-body">
        <ul class="list-group">
          <li v-for="report in reports" :key="report" class="list-group-item d-flex justify-content-between align-items-center">
            <span><i class="bi bi-file-earmark-bar-graph me-2"></i> {{ report }}</span>
            <a :href="getReportUrl(report)" target="_blank" class="btn btn-sm btn-outline-primary">
              View Report
            </a>
          </li>
          <li v-if="reports.length === 0" class="list-group-item text-muted text-center py-3">
            No monthly reports found. Click "Generate Report Now" to create one.
          </li>
        </ul>
      </div>
    </div>

  </div>
</template>

<script>
import api from '../../services/api';

export default {
  data() {
    return {
      stats: {},
      reports: [],
      generating: false
    };
  },
  async created() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        // 1. Get Stats
        const statsRes = await api.get('/admin/dashboard');
        this.stats = statsRes.data;

        // 2. Get list of reports from backend
        await this.fetchReports();
      } catch (err) {
        console.error('Failed to load dashboard data', err);
      }
    },

    async fetchReports() {
      try {
        // ✅ Calls the real backend route now
        const res = await api.get('/admin/reports');
        this.reports = res.data.reports;
      } catch (err) {
        console.error('Failed to fetch reports', err);
      }
    },

    async triggerReport() {
      this.generating = true;
      try {
        // ✅ Calls the real backend route to trigger Celery task
        await api.post('/admin/reports/generate');
        alert('Report generation started! It will appear in the list shortly.');

        // Wait a moment then refresh the list
        setTimeout(() => {
          this.fetchReports();
        }, 3000);
      } catch (err) {
        alert('Failed to trigger report generation');
        console.error(err);
      } finally {
        this.generating = false;
      }
    },

    getReportUrl(filename) {
      // ✅ Uses the authenticated admin route instead of /uploads/ directly
      return `http://localhost:5000/api/admin/reports/${filename}`;
    }
  }
};
</script>
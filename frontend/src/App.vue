<template>
  <div id="app">
    <h1>Financial Organizations</h1>
    <div v-if="organizations.length > 0">
      <OrganizationCard
        v-for="org in organizations"
        :key="org.id"
        :organization="org"
      />
    </div>
    <p v-else>Loading organizations...</p>
  </div>
</template>

<script>
import axios from 'axios';
import OrganizationCard from './components/OrganizationCard.vue';

export default {
  name: 'App',
  components: {
    OrganizationCard
  },
  data() {
    return {
      organizations: []
    };
  },
  mounted() {
    this.fetchOrganizations();
  },
  methods: {
    async fetchOrganizations() {
      try {
        const response = await axios.get('/api/organizations/');
        this.organizations = response.data;
      } catch (error) {
        console.error('Error fetching organizations:', error);
      }
    }
  }
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
</style>

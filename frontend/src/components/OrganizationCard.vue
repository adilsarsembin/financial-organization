<template>
  <div class="organization-card">
    <h2>{{ organization.name }}</h2>
    <p>{{ organization.org_type }} | {{ organization.address }}</p>
    <h3>News:</h3>
    <ul>
      <li v-for="news in organization.news" :key="news.source_url">
        <a :href="news.source_url" target="_blank">{{ news.title }}</a>
        <p>{{ news.summary }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'OrganizationCard',
  props: {
    organization: {
      type: Object,
      required: true
    }
  }
};
</script>

<style scoped>
.organization-card {
  border: 1px solid #ccc;
  padding: 16px;
  margin-bottom: 16px;
  border-radius: 4px;
}
a {
  color: #007bff;
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
</style>

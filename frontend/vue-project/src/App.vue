<script setup>
import SideBar from './components/Sidebar.vue';
import { defineComponent } from 'vue';
import { useRoute } from 'vue-router';

defineComponent({
  components: {
    SideBar,
  },
});
</script>

<template>
  <SideBar/>
  <main>
    <router-view/>
  </main>
</template>

<style scoped>
main {
  margin-left: 20vw; /* Adjust the margin as needed */
  padding: 0 2rem; /* Add some padding */
  /* Ensure the rest of the main content is visible */
  width: calc(100% - 20vw);
  height: 100%;
  overflow-y: auto; /* Add scrolling to the main content if needed */
}
</style>

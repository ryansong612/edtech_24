<script setup>
import SideBar from './components/Sidebar.vue';
import { defineComponent } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()

defineComponent({
  components: {
    SideBar,
  },
});
</script>

<template>
  <SideBar v-if="router.currentRoute.value.path != '/'"/>
  <Suspense>
  <main>
    <router-view/>
  </main>
  </Suspense>
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

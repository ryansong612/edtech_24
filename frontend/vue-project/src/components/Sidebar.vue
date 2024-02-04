<template>
    <ul>
      <li>
        <router-link to="/" active-class="active" @click="showTab('home')"><a href=""></a>New Generation</router-link>
    </li>
    <li>
      <router-link to="/class" active-class="active" @click="showTab('class')">Class</router-link>
    </li>
    <li>
      <router-link to="/database" active-class="active" @click="showTab('database')">Database</router-link>
    </li>
    </ul>
  </template>
  
  <script>
  export default {
    data() {
      return {
        activeTab: '',
      }
    },
    methods: {
      showTab(tab) {
        this.activeTab = tab;
      }
    }
  }
  </script>  

<style scoped>
ul {
    position: absolute;
    top: 0;
    left: 0;
    width: 20vw; /* Take the full width of the container */
    height: 100vh; /* Full height of the viewport */
    display: flex;
    flex-direction: column; /* Stack items vertically */
    justify-content: center; /* Center items on the cross-axis */
    align-items: center; /* Center items on the main-axis */
    background-color: rgba(255, 255, 255, 0.2); /* Dark background */
    
}

li {
    margin: 2rem 0; /* Add some space between the links */
}

a {
    color: rgba(255, 255, 255, 0.5); /* Light text color for links */
    text-decoration: none; /* No underline */
    font-size: 1.5rem; /* Larger text */
    transition: color 0.3s; /* Smooth color transition for hover effect */
}

a:hover, .active {
    color: white; /* Highlight color for active link and on hover */
}
</style>
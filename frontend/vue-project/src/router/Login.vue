<template>
<h1 class="home-page">Hi, are you a <router-link to="/student-home">student</router-link> or a <router-link to="/home">teacher</router-link>?</h1>
</template>

      
<style lang="scss" scoped>
.home-page {
      height: 100vh;
      display: flex;
      flex-direction: row;
      align-items: center;
      color: white;
      padding: 2rem;

    
.intro-section, .form-section {
      width: 50%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
      padding: 2rem;
      }

}
</style>
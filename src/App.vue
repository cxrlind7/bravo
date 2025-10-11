<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HomeView from './views/HomeView.vue';
import Whatsapp from './components/Whatsapp.vue';

</script>

<template>
  <RouterView />
  <Whatsapp />
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');

/* Estilos globales sin scoped */
* {
  font-family: 'Montserrat', sans-serif;
  box-sizing: border-box;
}

html, body {
  /* background-color: #dbdbdb; */
  margin: 0;
  padding: 0;
  font-family: 'Montserrat', sans-serif;
}
</style>
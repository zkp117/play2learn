<template>
  <div>
    <h1>Welcome to Math Facts!</h1>
    <AnagramHunt />
  </div>
</template>

<script>
import AnagramHunt from './apps/AnagramHunt.vue';

export default {
  name: 'App',
  components: {
    AnagramHunt
  }
}
</script>

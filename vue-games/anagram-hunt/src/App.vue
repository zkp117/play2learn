<template>
  <div>
    <h1 class="glitch-edit text-center">Anagram Hunt</h1>
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
<template>
  <AnagramHunt />
  <MathFacts />
</template>

<script>
import AnagramHunt from './apps/AnagramHunt.vue';
import MathFacts from './apps/MathFacts.vue';

export default {
  name: 'App',
  components: {
    MathFacts,
    AnagramHunt
  }
}
</script>

<style>

</style>

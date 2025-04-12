<template>
  <MathFacts />
  <AnagramHunt />
</template>

<script>
import MathFacts from './components/MathFacts.vue';
import AnagramHunt from './components/AnagramHunt.vue';

export default {
name: 'App',
components: {
  AnagramHunt,
  MathFacts,
}
}
</script>
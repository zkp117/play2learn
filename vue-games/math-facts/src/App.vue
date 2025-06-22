<template>
  <div>
    <h1 class="glitch-edit">Math Facts</h1>
    <MathGame />
  </div>
</template>

<script>
import MathGame from './MathFacts.vue'

export default {
  name: 'App',
  components: {
    MathGame
  }
}
</script>

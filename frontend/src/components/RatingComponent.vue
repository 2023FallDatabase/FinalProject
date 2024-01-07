<template>
  <div class="rating-system">
    <span v-for="star in 5" :key="star" class="star" @click="setRating(star)">
      {{ star <= rating ? '★' : '☆' }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'RatingComponent',
  props: ['initialRating'],
  data() {
    return {
      rating: this.initialRating
    };
  },
  methods: {
    setRating(star) {
      this.rating = star;
      this.$emit('update-rating', this.rating);
    }
  }
};
</script>

<style>
.star {
  cursor: pointer;
  color: gold;
}
</style>

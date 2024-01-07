<template>
  <div class="rating-system">
    <span v-for="star in maxStars" :key="star" class="star" @click="setRating(star)" :aria-label="'Star ' + star">
      {{ star <= rating ? '★' : '☆' }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'RatingComponent',
  props: {
    initialRating: {
      type: Number,
      default: 0,
      validator: (value) => value >= 0 && value <= 5
    },
    maxStars: {
      type: Number,
      default: 5
    }
  },
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

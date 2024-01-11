<template>
  <div class="rating-system">
    <span
      v-for="star in maxStars"
      :key="star"
      class="star"
      @click="setRating(star)"
      :aria-label="'Star ' + star"
    >
      {{ star <= rating ? "★" : "☆" }}
    </span>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "RatingComponent",
  props: {
    show_id: {
      type: String,
      default: "123"
    },
    initialRating: {
      type: Number,
      default: 0,
      validator: (value) => value >= 0 && value <= 5,
    },
    maxStars: {
      type: Number,
      default: 5,
    },
  },
  data() {
    return {
      rating: this.initialRating,
    };
  },
  methods: {
    setRating(star) {
      this.rating = star;
      let data=[];
      axios.get(`/api/AllForm/${this.show_id}`)
      .then(res=>{
        data=res.data;
        console.log(data.length);
      }).catch(err=>{
        console.log(err);
      })
      
      axios.patch(`/api/AllForm/${this.show_id}`,{
        star: this.rating
      }).then(res=>{
        console.log(res)
      }).catch(err=>{
        console.log(err)
      })
      
      console.log(this.rating);
      this.$emit("update-rating", this.rating);
    },
  },
};
</script>

<style>
.star {
  cursor: pointer;
  color: gold;
}
</style>
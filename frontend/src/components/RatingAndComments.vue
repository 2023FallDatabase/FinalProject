<!-- <template>
    <div class="rating-and-comments">
      <!-- Rating System -->
      <div class="rating-system">
        <span v-for="star in maxStars" :key="star" class="star" @click="setRating(star)" :aria-label="'Star ' + star">
          {{ star <= rating ? '★' : '☆' }}
        </span>
      </div>
  
      <!-- Comment Section -->
      <div class="comments-section">
        <div class="comments">
          <div v-for="comment in comments" :key="comment.id" class="comment">
            {{ comment.text }}
          </div>
        </div>
        <textarea v-model="newComment" placeholder="撰寫評論..."></textarea>
        <button @click="submitComment">提交評論</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'RatingAndComments',
    props: {
      initialRating: {
        type: Number,
        default: 0,
        validator: (value) => value >= 0 && value <= 5
      },
      comments: {
        type: Array,
        default: () => []
      }
    },
    data() {
      return {
        rating: this.initialRating,
        newComment: '',
        maxStars: 5 // Assuming a maximum of 5 stars
      };
    },
    methods: {
      setRating(star) {
        this.rating = star;
        this.$emit('update-rating', this.rating);
      },
      submitComment() {
        if (this.newComment.trim() === '') {
          alert('評論不能為空！');
          return;
        }
  
        const newComment = {
          id: Date.now(),
          text: this.newComment
        };
  
        this.comments.push(newComment);
        this.newComment = '';
      }
    }
  };
  </script>
  
  <style>
  .star {
    cursor: pointer;
    color: gold;
  }
  
  .comments {
    margin-bottom: 20px;
  }
  
  .comment {
    background-color: #f9bd78;
    padding: 10px;
    margin-bottom: 10px;
  }
  
  textarea {
    width: 100%;
    margin-bottom: 10px;
  }
  
  button {
    cursor: pointer;
  }
  </style>
   -->
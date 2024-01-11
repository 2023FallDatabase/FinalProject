<template>
  <div>
    <div class="comments">
      <div v-for="comment in comments" :key="comment.id" class="comment">
        {{ comment.text }}
      </div>
    </div>
    <textarea v-model="newComment" placeholder="撰寫評論..."></textarea>
    <button @click="submitComment">提交評論</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  props: {
    show_id: {
      type: String,
      default: "123"
    },
    comments: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      newComment: "",
    };
  },
  methods: {
    submitComment() {
      if (this.newComment.trim() === "") {
        alert("評論不能為空！");
        return;
      }
      console.log(this.show_id);
      axios.post(`/api/AllComment/${this.show_id}`,{
        show_id: this.show_id,
        comment: this.newComment
      })
      .then(response=>{
        console.log(response)
        
      }).catch(error=>{
        console.log(error)
      })
      // 創建一個新評論物件
      const newcomment = {
        id: Date.now(), // 假定每個評論都有一個唯一的ID
        text: this.newComment,
      };

      // 添加評論到現有評論列表
      const updatedComments = [...this.comments, newcomment];

      // 將新數組傳遞給父組件
      this.$emit("update:comments", updatedComments);

      // console.log(this.comments);
      // console.log(updatedComments);
      // 清空輸入框
      this.newComment = "";
    },
  },
};
</script>

<style>
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

<style>
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
<template>
  <div class="home-page">
    <h1>Home Page</h1>
    <form @submit.prevent="submitForm" class="form-container">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" :value="form.name" @input="$emit('update:form', { ...form, name: $event.target.value })" />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" :value="form.email" @input="$emit('update:form', { ...form, email: $event.target.value })" />
      </div>
      <div class="form-group">
        <label for="message">Message:</label>
        <textarea id="message" :value="form.message" @input="$emit('update:form', { ...form, message: $event.target.value })"></textarea>
      </div>
      <button type="submit" class="submit-button">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  props: {
    form: Object,
  },
  methods: {
    submitForm() {
      this.$emit('submitForm', this.form);
    },
  },
};
</script>

<style scoped>
.home-page {
  font-family: Arial, sans-serif;
  text-align: center;
  padding: 20px;
  max-width: 600px;
  margin: 0 auto;
}

.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
  width: 90%;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.form-group textarea {
  resize: vertical;
}

.submit-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  align-self: center;
}

.submit-button:hover {
  background-color: #0056b3;
}
</style>

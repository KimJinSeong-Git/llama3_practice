<template>
    <div>
      <h1>Home Page</h1>
      <form @submit.prevent="submitForm">
        <div>
          <label for="name">Name:</label>
          <input type="text" id="name" :value="form.name" @input="$emit('update:form', { ...form, name: $event.target.value })" />
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" :value="form.email" @input="$emit('update:form', { ...form, email: $event.target.value })" />
        </div>
        <div>
          <label for="message">Message:</label>
          <textarea id="message" :value="form.message" @input="$emit('update:form', { ...form, message: $event.target.value })"></textarea>
        </div>
        <button type="submit">Submit</button>
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
  
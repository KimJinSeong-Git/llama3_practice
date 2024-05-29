<template>
  <div class="home-page">
    <h1>Prompt Setting</h1>
    <form @submit.prevent="submitForm" class="form-container">
      <div class="form-group">
        <label for="context">Context (C):</label>
        <textarea id="context" :value="form.context" @input="$emit('update:form', { ...form, context: $event.target.value })" placeholder="Providing background information helps the LLM understand the specific scenario."></textarea>
        
      </div>
      <div class="form-group">
        <label for="objective">Output or Objective (O):</label>
        <textarea id="objective" :value="form.objective" @input="$emit('update:form', { ...form, objective: $event.target.value })" placeholder="Clearly defining the task directs the LLM’s focus."></textarea>
      </div>
      <div class="form-group">
        <label for="specificity">Specificity or Style (S):</label>
        <textarea id="specificity" :value="form.specificity" @input="$emit('update:form', { ...form, specificity: $event.target.value })" placeholder="Specifying the desired writing style aligns the LLM response."></textarea>
      </div>
      <div class="form-group">
        <label for="task">Task or Tone (T):</label>
        <textarea id="task" :value="form.task" @input="$emit('update:form', { ...form, task: $event.target.value })" placeholder="Setting the tone ensures the response resonates with the required sentiment."></textarea>
      </div>
      <div class="form-group">
        <label for="assumptions">Assumptions or Audience (A):</label>
        <textarea id="assumptions" :value="form.assumptions" @input="$emit('update:form', { ...form, assumptions: $event.target.value })" placeholder="Identifying the intended audience tailors the LLM’s response to be targeted to an audience."></textarea>
      </div>
      <div class="form-group">
        <label for="requirements">Requirements or Response (R):</label>
        <textarea id="requirements" :value="form.requirements" @input="$emit('update:form', { ...form, requirements: $event.target.value })" placeholder="Providing the response format, like text or json, ensures the LLM outputs, and help build pipelines."></textarea>
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
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 15px;
  width: 100%;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input,
.form-group textarea {
  width: 100%;
  height: 80px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  resize: none;
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
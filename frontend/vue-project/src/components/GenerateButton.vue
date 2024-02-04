<script>
import { ref, onMounted } from 'vue';
export default {
    emits: ['submit'],
  methods: {
    handleSubmit() {
      this.$emit('submit');
    },
  },
  setup() {
    const textarea = ref(null);

    const autoExpand = () => {
      textarea.value.style.height = 'auto';
      const newHeight = textarea.value.scrollHeight + 'px';
      textarea.value.style.height = newHeight;
      // If the scrollHeight is greater than max-height, it will become scrollable
      if (textarea.value.scrollHeight > textarea.value.style.maxHeight.replace('px', '')) {
        textarea.value.style.overflowY = 'auto';
      }
    };

    onMounted(() => {
      // Initial adjustment if the textarea contains content when it's mounted
      autoExpand();
    });

    return {
      textarea,
      autoExpand
    };
  }
}
</script>
<template lang="pug">
.input-box
    .title Generate new paper's using prompt
    textarea(
        ref="textarea"
        @input="autoExpand"
        placeholder="Enter the topic you want to generate: Eg: I want to practice on simple object-oriented questions using multiple choices"
    )
    button.submit-button(@click="handleSubmit") Submit
</template>
<style scoped lang="scss">
.input-box {
        position: relative;
        background-color: #4a4a4a; // Dark gray background
        border-radius: 10px; // Rounded corners
        padding: 20px; // Padding around the content
        margin: 20px 0; // Vertical margin
        width: 100%; // Full width
        box-sizing: border-box; // Include padding and border in the element's width and height
        overflow: auto;

        .title {
            color: #fff; // White text
            font-size: 1.125rem; // Relative font size
            margin-bottom: 1rem; // Space below title
        }

        textarea {
            width: calc(100% - 30px); // Full width of the parent minus padding
            max-height: 8em;
            padding: 10px 15px; // Padding inside the textarea
            padding-right: 8em;
            border: 1px solid #ccc; // Light gray border
            box-sizing: border-box; // Include padding and border in the element's width and height
            border-radius: 5px; // Rounded corners for the textarea
            font-size: 1rem; // Relative font size
            color: #4a4a4a;
            background-color: #fff; // White background for visibility
            resize: vertical; // Allow only vertical resizing
        }

        button.submit-button {
            position: absolute;
            right: 4em;
            bottom: 2.5em;
            border: none;
            background-color: #4CAF50; // Green background
            color: white;
            padding: 10px 20px; // Padding inside the button
            border-radius: 5px; // Rounded corners for the button
            font-size: 1rem; // Relative font size
            transition: background-color 0.3s; // Smooth transition for background color

            &:hover {
            background-color: #45a049; // Darker green background on hover
            }
        }

        // Clear floats
        &::after {
            content: "";
            clear: both;
            display: table;
        }
    }


    button.submit-button {
    border: none;
    background-color: purple;
    /* Purple background */
    color: white;
    padding: 0.5em 1em;
    cursor: pointer;
}

button.submit-button:hover {
    background-color: #8e44ad;
    /* Lighter purple background on hover */
}
</style>
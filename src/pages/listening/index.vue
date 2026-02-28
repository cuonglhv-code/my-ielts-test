<script setup>
const scoreTable = [
  ['39-40', '9.0'],
  ['37-38', '8.5'],
  ['35-36', '8.0'],
  ['33-34', '7.5'],
  ['30-32', '7.0'],
  ['27-29', '6.5'],
  ['23-26', '6.0'],
  ['20-22', '5.5'],
  ['16-19', '5.0'],
  ['13-15', '4.5'],
  ['10-12', '4.0'],
  ['6-9', '3.5'],
  ['4-5', '3.0'],
  ['3', '2.5'],
  ['2', '2.0'],
  ['1', '1.0'],
  ['absent', '0.0'],
]
</script>

<template>
  <div class="px-4 pt-6 text-gray-500 2xl:px-0 dark:text-gray-400">
    <h3 class="mb-4 text-xl font-semibold text-black dark:text-white">
      Overview
    </h3>
    <div class="mb-4">
      <p>Understand IELTS listening and some basic principles and techniques in the exam</p>
      <br>
      <p>Rating table</p>
      <table class="w-full text-center text-sm text-gray-500 dark:text-gray-400">
        <tbody>
          <tr class="border bg-white dark:border-gray-700 dark:bg-gray-800">
            <td v-for="v in scoreTable" :key="v[0]" class="border px-6 py-4">
              {{ v[0] }}
            </td>
          </tr>
          <tr class="border bg-white dark:border-gray-700 dark:bg-gray-800">
            <td v-for="v in scoreTable" :key="v[0]" class="border px-6 py-4">
              {{ v[1] }}
            </td>
          </tr>
        </tbody>
      </table>
      <br>
      <ul class="ml-6 list-disc">
        <li>Time limit 30min</li>
        <li>10 minutes extra time at the end (this should be a written test, the computer test may be different)</li>
        <li>40 questions (you can get 7+ if you make less than 10 mistakes)</li>
        <li>4 sections, 10 questions each, increasing difficulty</li>
        <li>Answers are sequential</li>
        <li>
          3 question types
          <ul class="ml-6 list-disc">
            <li>gap-fill </li>
            <li>Multiple choice multiple choice questions (not multiple choice questions, but choose one from multiple options)</li>
            <li>matching matching</li>
          </ul>
        </li>

        <li>Multiple accents</li>
        <li>You can only listen once! ! ! </li>
      </ul>
    </div>
    <h3 class="my-4 text-xl font-semibold text-black dark:text-white">
      Section 1
    </h3>
    <ul class="mb-4 ml-6 list-disc">
      <li>Conversation between 2 people</li>
      <li>
        Simple daily communication
        <ul class="ml-6 list-disc">
          <li>e.g. making a booking</li>
        </ul>
      </li>
      <li>A speaker gives basic information</li>
      <li>Simple fill-in-the-blank questions: complete the missing information</li>
      <li>
        The information is generally
        <ul class="ml-6 list-disc">
          <li>names</li>
          <li>addresses</li>
          <li>dates</li>
          <li>times</li>
          <li>numbers</li>
        </ul>
      </li>
      <li>The first section is very easy. You must get a high score of 9-10 correct answers. This will give you more room for mistakes in the later difficult parts</li>
    </ul>
    <p><strong>Key Tips:</strong></p>
    <ul class="ml-6 list-disc">
      <li>Use the breaks to read ahead Use the breaks to read ahead of time</li>
      <li>Before each section starts Pause before each section starts</li>
      <li>In the middle of each section (Except in section 4) The pause in the middle of each section, there is no pause in the fourth section</li>
      <li>At the end of each section</li>
      <li>Don't check back, read ahead Don't check back, read ahead! Don't look behind you! Don't look behind you! If you miss it, you miss it</li>
    </ul>

    <h3 class="my-4 text-xl font-semibold text-black dark:text-white">
      Section 2
    </h3>
    <ul class="ml-6 list-disc">
      <li>Use all of the break time at the end of section 1 Read the questions of the second section immediately after the end of the first section</li>
      <li>Only one speaker</li>
      <li>
        A simple statement on a non-academic topic:
        <ul class="ml-6 list-disc">
          <li>Tourism</li>
          <li>A park</li>
          <li>Local facilities</li>
        </ul>
      </li>
      <li>Question types: fill in the blanks, selection, matching</li>
      <li>There will be a pause in the middle (usually you will be asked to read the first 5 questions first, and there will be a pause in the middle to let you read the next 5 questions)</li>
      <li>Still quite easy, aim for a high score The difficulty is low, you still need to strive for a high score</li>
    </ul>

    <h3 class="my-4 text-xl font-semibold text-black dark:text-white">
      Section 3
    </h3>

    <ul class="ml-6 list-disc">
      <li>Use breaks to read and underline Use breaks to read questions and underline keywords</li>
      <li>2-3 personal conversations</li>
      <li>The dialogue will be related to education and training, for example: teacher and 2 students</li>
      <li>Gap-fill, multiple choice (difficult) Question type: fill in the blank, multiple choice (difficult)</li>
      <li>Underline keywords in questions and choices Underline keywords in questions and choices</li>
      <li>Listen for keywords or synonyms Listen for keywords or corresponding synonyms</li>
      <li>For difficult sections, the goal should be 6-7 correct answers</li>
    </ul>

    <h3 class="my-4 text-xl font-semibold text-black dark:text-white">
      Section 4
    </h3>
    <ul class="ml-6 list-disc">
      <li>Use the gaps in the third section to read questions</li>
      <li>Underline keywords</li>
      <li>There is no pause in the middle of this section. The title and key words should be read and crossed as much as possible</li>
      <li>Only one person said it</li>
      <li>Content academically relevant</li>
      <li>Question type: fill in the blank, choice</li>
      <li>Listen to keywords or corresponding synonyms</li>
      <li>Difficult: faster speech, more content, extra information Difficult: faster speech, more content, a lot of extra information. For example: 30s of voice may not give any answer</li>
    </ul>

    <h3 class="my-4 text-xl font-semibold text-black dark:text-white">
      Summary
    </h3>
    <p>Do some real practice tests mock exam practice</p>
    <ol class="ml-6 list-decimal">
      <li>Read ahead (only check back at the end) Read the questions forward and check back only at the end of the entire listening session</li>
      <li>Underline keywords Underline keywords. Underline keywords when reading questions</li>
      <li>Listen for keywords or synonyms Pay attention to keywords or their corresponding synonyms</li>
      <li>Be careful with spelling, even if you hear it and spell it incorrectly, it won’t matter</li>
      <li>Don’t get stuck on a difficult question - move forward Don’t get stuck on a difficult question, move forward</li>
      <li>Concentrate! Give your full attention for 30 minutes</li>
    </ol>
  </div>
</template>

<style>
  .dark svg text {
    font-family:"comic sans ms", system-ui;
    fill: #fff;
  }
</style>

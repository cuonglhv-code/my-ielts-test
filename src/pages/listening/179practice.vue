<script setup>import words from './listening179.json'

const ws = reactive(words.map((v) => {
  const item = {
    ...v,
    form: {
      word: '',
      replaceStr: '',
    },
    result: {
      checked: false,
      errorWords: [],
    },
  }
  return item
}))

function onKeydown(e, word) {
  if (e.key === '`') {
    e.preventDefault()
    play(word)
  }
}

function play(word) {
  const audio = document.createElement('audio')
  audio.src = `/179_audios/${word}.mp3`
  audio.play()
}
function next(index) {
  const i = index + 1
  if (i >= words.length)
    return

  //Verification results
  const cw = ws[index]

  // Process words
  const practiceWord = cw.form.word.trim().toLowerCase()
  const practiceReplace = cw.form.replaceStr.split(/[,,]/).map(v => v.trim().toLowerCase().replace(/\s+/g,' '))
  // window.console.log(practiceReplace, practiceWord)

  const errorWords = []
  if (practiceWord !== cw.word)
    errorWords.push(cw.word)

  errorWords.push(...cw.replace.filter((w) => {
    return !practiceReplace.includes(w)
  }))
  cw.result.checked = true
  cw.result.errorWords = errorWords

  // window.console.log(cw)

  const nw = words[i]
  play(nw.word)
  //Move the cursor to the next input box
  document.getElementById(`input_${i + 1}`)?.focus()
}</script>

<template>
  <div>
    <div class="mt-6 items-center justify-between lg:flex">
      <div class="mb-4 lg:mb-0">
        <h3 class="mb-2 text-xl font-bold text-gray-900 dark:text-white">
          Listening 179 test word practice
        </h3>
        <ul class="ml-4 list-decimal text-sm font-normal text-gray-500 dark:text-gray-400">
          <li>Use English commas to synonymously replace multiple words <kbd class="rounded-lg bg-gray-100 px-2 text-xs font-semibold text-gray-800 dark:border-gray-500 dark:bg-gray-600 dark:text-gray-100">,</kbd> Split</li>
          <li>The audio will switch to the next word, click the speaker icon, and press the button <kbd class="rounded-lg bg-gray-100 px-2 text-xs font-semibold text-gray-800 dark:border-gray-500 dark:bg-gray-600 dark:text-gray-100">`</kbd>(The one to the left of the number 1) Play</li>
          <li>After entering the test word, press Tab to switch to synonyms. After entering the synonym, press Enter to automatically check and switch to the next word</li>
          <li>There are multiple spaces between words, and whether there are spaces after the comma does not affect the result judgment</li>
        </ul>
      </div>
      <div class="items-center sm:flex">
        <div class="flex items-center">
          <button
            type="button"
            class="rounded-lg bg-blue-700 px-5 py-2.5 text-sm font-medium text-white dark:bg-blue-600 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            @click="() => { play(words[0].word) }">
            start
          </button>
        </div>
      </div>
    </div>
    <div class="relative mt-4 overflow-x-auto">
      <table class="w-full text-left text-sm text-gray-500 dark:text-gray-400">
        <thead class="bg-gray-50 text-xs uppercase text-gray-700 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th class="w-0 px-6 py-3">
              #
            </th>

            <th class="w-0 px-6 py-3">
              part of speech
            </th>
            <th class="w-20 px-6 py-3">
              Audio
            </th>
            <th class="px-6 py-3">
              Test word/synonym replacement
            </th>
            <th class="px-6 py-3">
              result
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(w, i) in ws" :key="w.index" class="border-b bg-white dark:border-gray-700 dark:bg-gray-800">
            <td class="px-6 py-4">
              {{ w.index }}
            </td>
            <td class="px-6 py-4 italic">
              {{ w.type }}
            </td>
            <td class="px-6 py-4">
              <button class="i-carbon-volume-up-filled" @click="play(w.word)" />
            </td>
            <td
              class="flex flex-row items-center justify-start px-6 py-4"
              @keydown="onKeydown($event, w.word)"
            >
              <input
                :id="`input_${w.index}`"
                v-model="w.form.word"
                p="x-2 y-1"
                w="150px"
                bg="transparent"
                border="~ rounded gray-200 dark:gray-700"
                outline="none active:none"
                spellcheck="false"
                type="text"
                placeholder="Please enter..."
              >
              <div class="px-4">
                {{ w.meaning }}
              </div>
              <input
                v-model="w.form.replaceStr"
                p="x-2 y-1"
                w="300px"
                bg="transparent"
                border="~ rounded gray-200 dark:gray-700"
                outline="none active:none"
                type="text"
                spellcheck="false"
                placeholder="Please enter..."
                @keydown.enter="next(i)"
              >
            </td>
            <td class="px-6 py-4">
              <i v-if="w.result.checked && w.result.errorWords.length < 1" class="i-carbon-checkmark block text-green-700" />
              <p v-if="w.result.checked && w.result.errorWords.length > 0">
                {{ w.result.errorWords.join(', ') }}
              </p>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

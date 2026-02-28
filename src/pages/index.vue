<script setup lang="ts" generic="T extends any, O extends any">
import { RouterLink } from 'vue-router'

defineOptions({
  name: 'IndexPage',
})

const menus = reactive([
  {
    label: 'Vocabulary',
    icon: 'i-carbon-chart-histogram',
    link: '/vocabulary',
    desc: 'Contains IELTS vocabulary materials, grouped by scenario',
  },
  {
    label: 'Grammar',
    icon: 'i-carbon-load-balancer-vpc ',
    link: '/grammar',
    desc: 'New Oriental IELTS grammar course, mind map',
  },
  {
    label: 'Listening',
    icon: 'i-carbon-headphones',
    link: '/listening',
    desc: 'Basic listening concepts, 179 testing points synonym replacements and corpus',
  },
  {
    label: 'Speaking',
    icon: 'i-carbon-microphone',
    link: '/speaking',
    desc: 'TODO Maybe add logical chain related content',
  },
  {
    label: 'Reading',
    icon: 'i-carbon-white-paper',
    link: '/reading',
    desc: '538 testing points synonym replacements',
  },
  {
    label: 'Writing',
    icon: 'i-carbon-edit',
    link: '/writing',
    desc: '100 sentence translation practice, task 1 and task 2',
  },
])
</script>

<template>
  <div class="px-4 pt-6 2xl:px-0">
    <section class="mb-4 border border-gray-200 rounded-lg bg-white p-4 shadow-sm dark:border-gray-700 dark:bg-gray-800 sm:p-6">
      <div class="mx-auto max-w-screen-xl px-4 py-8 lg:px-6 sm:py-16">
        <h1 style="font-family: Charmonman;" class="mb-16 text-center text-6xl text-gray-900 dark:text-white">
          Salvation lies within <span class="font-bold text-#f00">IELTS</span>
        </h1>
        <div class="mb-8 max-w-screen-md lg:mb-16">
          <h2 class="mb-4 text-4xl font-extrabold tracking-tight text-gray-900 dark:text-white">
            My IELTS Preparation Center
          </h2>
          <p class="text-gray-500 sm:text-xl dark:text-gray-400">
            Hello, This is Frank. This contains everything for my test preparation, starting from vocabulary, grammar...
          </p>
        </div>
        <div class="md:grid lg:grid-cols-3 md:grid-cols-2 md:gap-12 space-y-8 md:space-y-0">
          <RouterLink
            v-for="m in menus"
            :key="m.label"
            :to="m.link"
            class="block"
          >
            <div class="mb-4 h-10 w-10 flex items-center justify-center rounded-full bg-primary-100 lg:h-12 lg:w-12 dark:bg-primary-900">
              <i class="block h-5 w-5 text-primary-600 lg:h-6 lg:w-6 dark:text-primary-300" :class="m.icon" />
            </div>
            <h3 class="mb-2 text-xl font-bold dark:text-white">
              {{ m.label }}
            </h3>
            <p class="text-gray-500 dark:text-gray-400">
              {{ m.desc }}
            </p>
          </RouterLink>
        </div>
      </div>
    </section>
  </div>
</template>

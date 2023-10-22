<template>
  <div class="max-w-3xl py-12 mx-auto">
    <ul>
      <li v-for = "dd in ddd.data ">
        {{ dd.mobile_number }}
      </li>
    </ul>
      
  </div>
</template>

<script>
//import { ref } from 'vue'
import { Dialog } from 'frappe-ui'
import { createResource } from 'frappe-ui'
import { session } from '../data/session'


// const ping = createResource({
//   url: 'ping',
//   auto: true,
// })
const ddd = createResource({
  doctype: 'driver_location_demo',
  fields: ['mobile_number'],
  limits: 10
})

ddd.reload()

</script>

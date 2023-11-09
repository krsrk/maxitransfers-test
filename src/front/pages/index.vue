<template>
  <div>
    <h2>
      Empleados
    </h2>
    <v-row>
      <v-col cols="6">
        <v-sheet rounded="lg">
          <TheItems :data="data"/>
        </v-sheet>
      </v-col>
      <v-col>
        <v-sheet rounded="lg">
          <TheForm />
        </v-sheet>
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts" setup>
import { computed } from 'vue'
import { useEmployeeStore } from "~/src/stores/EmployeeStore"

onBeforeMount( () => {
    store.getEmployees()
})

const store = useEmployeeStore()

const data = computed(() => store.getEmployeesData)
</script>
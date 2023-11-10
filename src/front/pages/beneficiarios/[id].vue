<template>
  <div>
    <h2>
      Beneficiarios del Empleado {{ employee[1] }}
    </h2>
    <v-row>
      <v-col cols="6">
        <v-sheet rounded="lg">
          <TheItems :data="data" :beneficiary-context="true"/>
        </v-sheet>
      </v-col>
      <v-col>
        <v-sheet rounded="lg">
          <TheForm :beneficiary-context="true"/>
        </v-sheet>
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts" setup>
import { computed, ref } from 'vue'
import { useBeneficiaryStore } from "~/src/stores/BeneficiaryStore"
import { useFormStore } from "~/src/stores/FormStore"

const route = useRoute()
const store = useBeneficiaryStore()
const formStore = useFormStore()
const employee = route.params.id.split('-')

formStore.$state.formTitle = 'Agregar Beneficiario'

onBeforeMount( () => {
    store.getBeneficiaries(employee[0])
})

const data = computed(() => store.getBeneficiariesData)
</script>
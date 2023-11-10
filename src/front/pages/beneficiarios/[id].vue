<template>
  <div>
    <v-row>
      <v-col cols="12">
        <a href="/" type="button" class="secondary mt-2">
            Regresar
        </a>
      </v-col>
    </v-row>
    <h2>
      Beneficiarios del Empleado {{ employee[1] }}
    </h2>
    <v-row>
      <v-col cols="6">
        <v-sheet rounded="lg">
          <TheItems
              :data="data"
              :beneficiary-context="true"
              @edit-item-action="setFormData"
              @delete-item-action="deleteItemClickHandler"
          />
        </v-sheet>
      </v-col>
      <v-col>
        <v-sheet rounded="lg">
          <TheForm
              :beneficiary-context="true"
              @submit-form="sendFormToCreateService"
              @submit-edit-form="sendFormToUpdateService"
          />
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
const data = computed(() => store.getBeneficiariesData)

formStore.$state.formTitle = 'Agregar Beneficiario'

onBeforeMount( () => {
    store.getBeneficiaries(employee[0])
})

const sendFormToCreateService = async (form:any) => {
  await store.createBeneficiary(employee[0], form)
}

const sendFormToUpdateService = async (form:any) => {
  await store.updateBeneficiary(employee[0], form)
}

const setFormData = async (it: any) => {
  await formStore.setBeneficiaryForm(it)
  formStore.$state.editForm = true
  formStore.$state.formTitle = 'Editar Beneficiario'
  formStore.$state.formButtonTitle = 'Editar'
}

const deleteItemClickHandler = async (it:any) => {
  await store.deleteBeneficiary(employee[0], it.id)
}
</script>
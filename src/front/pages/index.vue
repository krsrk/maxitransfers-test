<template>
  <div>
    <h2>
      Empleados
    </h2>
    <v-row>
      <v-col cols="6">
        <v-sheet rounded="lg">
          <TheItems
              :data="data"
              :beneficiary-context="false"
              @edit-item-action="setFormData"
              @delete-item-action="deleteItemClickHandler"
          />
        </v-sheet>
      </v-col>
      <v-col>
        <v-sheet rounded="lg">
          <TheForm
              :beneficiary-context="false"
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
import { useEmployeeStore } from "~/src/stores/EmployeeStore"
import { useFormStore } from "~/src/stores/FormStore"

onBeforeMount( () => {
    store.getEmployees()
})

const store = useEmployeeStore()
const formStore = useFormStore()
const data = computed(() => store.getEmployeesData)

const sendFormToCreateService = async (form:any) => {
  await store.createEmployee(form)
}

const sendFormToUpdateService = async (form:any) => {
  await store.updateEmployee(form)
}

const setFormData = async (it: any) => {
  await formStore.setForm(it)
  formStore.$state.editForm = true
  formStore.$state.formTitle = 'Editar Empleado'
  formStore.$state.formButtonTitle = 'Editar'
}

const deleteItemClickHandler = async (it:any) => {
  await store.deleteEmployee(it.id)
}
</script>
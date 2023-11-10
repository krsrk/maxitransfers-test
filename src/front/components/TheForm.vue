<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12" md="12">
          <h2>{{ formTitle }}</h2>
        </v-col>
      </v-row>
      <v-row>
        <v-col
            cols="12"
            md="6"
        >
          <v-text-field
              v-model="form.name"
              label="Nombre"
              required
              hide-details
          ></v-text-field>
        </v-col>

        <v-col
            cols="12"
            md="6"
        >
          <v-text-field
              v-model="form.last_name"
              label="Apellidos"
              hide-details
              required
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col
            cols="12"
            md="6"
        >
          <v-text-field
              v-model="form.birth_date"
              label="Fecha Nacimiento"
              hide-details
              required
          ></v-text-field>
        </v-col>
        <template v-if="!props.beneficiaryContext">
          <v-col
              cols="12"
              md="6"
          >
            <v-text-field
                v-model="form.employee_number"
                label="No. Empleado"
                hide-details
                required
            ></v-text-field>
          </v-col>
        </template>
        <template v-else>
          <v-col
              cols="12"
              md="6"
          >
            <v-text-field
                v-model="form.participation_percentage"
                label="Porcentaje de Participación"
                hide-details
                required
            ></v-text-field>
          </v-col>
        </template>
      </v-row>

      <v-row>
        <v-col
            cols="12"
            md="6"
        >
          <v-text-field
              v-model="form.curp"
              label="CURP"
              hide-details
              required
          ></v-text-field>
        </v-col>

        <v-col
            cols="12"
            md="6"
        >
          <v-text-field
              v-model="form.ssn"
              label="SSN"
              hide-details
              required
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col
            cols="12"
            md="6"
        >
          <v-text-field
              v-model="form.phone_number"
              label="Teléfono"
              hide-details
              required
          ></v-text-field>
        </v-col>

        <v-col
            cols="12"
            md="6"
        >
          <v-text-field
              v-model="form.nationality"
              label="Nacionalidad"
              hide-details
              required
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="6">
          <v-btn type="submit" block class="secondary mt-2" @click.prevent="clearForm">
            Limpiar
          </v-btn>
        </v-col>

        <v-col cols="12" md="6">
          <v-btn type="submit" block class="secondary mt-2" @click.prevent="submitForm">
            {{ formBtnTitle }}
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script lang="ts" setup>
import { useFormStore } from "~/src/stores/FormStore"

const store = useFormStore()
const props = defineProps({ beneficiaryContext: Boolean })
const emit = defineEmits(['submitForm', 'submitEditForm'])
const form = computed(() => store.$state.form)
const formTitle = computed(() => store.$state.formTitle)
const formBtnTitle = computed(() => store.$state.formButtonTitle)
const editForm = computed(() => store.$state.editForm)

const submitForm = async () => {
  //validate form before emit
  if (!editForm.value) {
    await emit('submitForm', form.value)
  } else {
    await emit('submitEditForm', form.value)
  }

  await clearForm()
}

const clearForm = async () => {
  await store.setForm({})
  store.$state.editForm = false
  store.$state.formTitle = 'Agregar Empleado'
  store.$state.formButtonTitle = 'Agregar'
}
</script>
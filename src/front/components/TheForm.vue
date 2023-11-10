<template>
  <v-form v-model="validForm">
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
              :rules="requiredRules"
          ></v-text-field>
        </v-col>

        <v-col
            cols="12"
            md="6"
        >
          <v-text-field
              v-model="form.last_name"
              label="Apellidos"
              :rules="requiredRules"
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
              placeholder="AAAA-mm-dd"
              :rules="birthdateRules"
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
                :rules="requiredRules"
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
                :rules="requiredRules"
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
              :rules="requiredRules"
          ></v-text-field>
        </v-col>

        <v-col
            cols="12"
            md="6"
        >
          <v-text-field
              v-model="form.ssn"
              label="SSN"
              :rules="requiredRules"
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
              :rules="phoneRules"
          ></v-text-field>
        </v-col>

        <v-col
            cols="12"
            md="6"
        >
          <v-text-field
              v-model="form.nationality"
              label="Nacionalidad"
              :rules="requiredRules"
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
import {useFormStore} from "~/src/stores/FormStore"
import {useBeneficiaryStore} from "~/src/stores/BeneficiaryStore"

const store = useFormStore()
const beneficiaryStore = useBeneficiaryStore()
const props = defineProps({beneficiaryContext: Boolean})
const emit = defineEmits(['submitForm', 'submitEditForm'])
const form = computed(() => store.$state.form)
const formTitle = computed(() => store.$state.formTitle)
const formBtnTitle = computed(() => store.$state.formButtonTitle)
const editForm = computed(() => store.$state.editForm)
const validForm = ref(false)

const birthdateRules = ref([
  (value: any) => {
    if (value) return true

    return 'Campo requerido.'
  },
  (value: any) => {
    const now = new Date()
    let birthdate = new Date(value)
    let age = now.getFullYear() - birthdate.getFullYear()
    let m = now.getMonth() - birthdate.getMonth()
    if (m < 0 || (m === 0 && now.getDate() < birthdate.getDate())) {
      age--;
    }

    if (age >= 18) return true

    return 'Debes ser mayor de edad'
  },
])

const phoneRules = ref([
  (value: any) => {
    if (value) return true

    return 'Campo requerido.'
  },
  (value: any) => {
    if (value?.length == 10 && /[0-9-]+/.test(value)) return true

    return 'Telefono solo debe 10 digitos.'
  }
])

const requiredRules = ref([
  (value: any) => {
    if (value) return true

    return 'Campo requerido.'
  }
])

const submitForm = async () => {
  if (!validForm.value) {
    alert('Hay errores en el formulario')
    return
  }

  if (beneficiaryStore.isParticipationPercentageOutOfLimit(editForm.value, form.value)) {
    alert('Se supero el limite de 100 en porcentaje de participación')
    return
  }

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
  store.$state.formTitle = (props.beneficiaryContext) ? 'Agregar Beneficiario' : 'Agregar Empleado'
  store.$state.formButtonTitle = 'Agregar'
}
</script>
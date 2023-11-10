<template>
  <div>
    <v-table
        fixed-header
        height="500px"
    >
      <thead>
      <tr>
        <template v-if="!props.beneficiaryContext">
          <th class="text-left">
            No. Empleado
          </th>
        </template>

        <th class="text-left">
          Nombre
        </th>
        <template v-if="props.beneficiaryContext">
          <th class="text-left">
            Porcentaje de Participación
          </th>
        </template>
        <th class="text-left">
          Acciones
        </th>
      </tr>
      </thead>
      <tbody>
      <tr
          v-for="item in props.data"
          :key="item.id"
      >
        <template v-if="!props.beneficiaryContext">
          <td>{{ item.employee_number }}</td>
        </template>

        <td>{{ item.name + ' ' +item.last_name}}</td>

        <template v-if="props.beneficiaryContext">
          <td>{{ item.participation_percentage }}</td>
        </template>

        <td>
          <v-icon
              size="small"
              class="me-2"
              @click="editItemClickHandler(item)"
          >
            mdi-pencil
          </v-icon>
          <template v-if="!props.beneficiaryContext">
            <v-icon
                size="small"
                class="me-2"
                @click="goToBeneficiariesPageClickHandler(item)"
            >
              mdi-account-details
            </v-icon>
          </template>
          <v-icon
              size="small"
              @click="deleteItemClickHandler(item)"
          >
            mdi-delete
          </v-icon>
        </td>
      </tr>
      </tbody>
    </v-table>
  </div>
</template>

<script lang="ts" setup>
const emit = defineEmits(['editItemAction', 'deleteItemAction'])
const props = defineProps({ data: Array, beneficiaryContext: Boolean })

const editItemClickHandler = (it:any) => {
  emit('editItemAction', it)
}

const deleteItemClickHandler = (it:any) => {
  emit('deleteItemAction', it)
}

const goToBeneficiariesPageClickHandler = async (it:any) => {
  await navigateTo('/beneficiarios/' + it.id + '-' + it.name)
}
</script>
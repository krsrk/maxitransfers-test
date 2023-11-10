<template>
  <div>
    <v-table
        fixed-header
        height="500px"
    >
      <thead>
      <tr>
        <th class="text-left">
          No. Empleado
        </th>
        <th class="text-left">
          Nombre
        </th>
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
        <td>{{ item.employee_number }}</td>
        <td>{{ item.name + ' ' +item.last_name}}</td>
        <td>
          <v-icon
              size="small"
              class="me-2"
              @click="editItemClickHandler(item)"
          >
            mdi-pencil
          </v-icon>
          <v-icon
              size="small"
              class="me-2"
              @click="editItem(item)"
          >
            mdi-account-details
          </v-icon>
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
import {ref} from 'vue';

const emit = defineEmits(['editItemAction', 'deleteItemAction'])
const props = defineProps({ data: Array })

const editItemClickHandler = (it:any) => {
  emit('editItemAction', it)
}

const deleteItemClickHandler = (it:any) => {
  emit('deleteItemAction', it)
}
</script>
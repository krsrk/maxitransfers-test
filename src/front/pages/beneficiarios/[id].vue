<template>
  <div>
    <h2>
      Beneficiarios Empleado {{ idEmpleado }}
    </h2>
  </div>
</template>

<script lang="ts" setup>
const route = useRoute()
const idEmpleado = route.params.id

</script>
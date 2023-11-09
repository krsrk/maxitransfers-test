<template>
    <v-app id="inspire">

        <v-app-bar color="primary">
          <v-app-bar-title>Admin Empleados</v-app-bar-title>
        </v-app-bar>

        <v-main class="bg-grey-lighten-3">
            <v-container>
                <slot />
            </v-container>
        </v-main>
    </v-app>
</template>
<template>
    <v-app id="inspire">

        <v-app-bar color="primary">
          <v-app-bar-title>Admin Empleados</v-app-bar-title>
        </v-app-bar>

        <v-main>
            <v-container>
                <slot />
            </v-container>
        </v-main>
    </v-app>
</template>
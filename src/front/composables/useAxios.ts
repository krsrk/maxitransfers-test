import {useNuxtApp} from "#app";

export const useAxiosRequest = () => {
    return useNuxtApp().$axios
}
import { FormEvent, useEffect, useRef } from 'react';
import { FormCategoriesProps } from '../entity/interfaces';
import { api, getCategories } from '../services/apis';


export default function FormCategories({ setCategories }: FormCategoriesProps) {
  const nameRef = useRef<HTMLInputElement | null>(null)

  useEffect(() => {
    loadCategories()
  }, [])

  async function loadCategories() {
    setCategories(await getCategories())
  }

  async function handleSubmit(event: FormEvent){
    event.preventDefault()
    if (
      !nameRef.current?.value
      ) {
        return;
      }


    const response = await api.post("/categories/", {
      name: nameRef.current?.value,
    }
    )

    setCategories(allCategories=> [...allCategories, response.data])

    nameRef.current.value = ""
  }

    return (
        <form className="flex flex-col my-6 mb-8" onSubmit={handleSubmit}>
          <label className="font-medium text-white">Descrição:</label>
          <input type="text"
          name="name" id="id_name"
          placeholder="Nome da categoria..."
          className="w-full mb-5 p-2 rounded"
          ref={nameRef}
          />
          <input type="submit" value="Registar" className="cursor-pointer w-full p-2 bg-green-500 rounded font-medium"/>
        </form>
    )
}
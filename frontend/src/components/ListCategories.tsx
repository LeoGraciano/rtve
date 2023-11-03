import { useEffect, useState } from 'react';
import { FiTrash } from 'react-icons/fi';
import { CategoriesProps, ListCategoriesProps } from '../entity/interfaces';
import { api, getCategories } from '../services/apis';
import FormCategories from './FormCategories';


export default function ListCategories({ isForm }: ListCategoriesProps) {
  const [categories, setCategories] = useState<CategoriesProps[]>([])

  useEffect(() => {
    loadCategories()
  }, [])

  async function loadCategories() {
    setCategories(await getCategories())
  }


  async function handleDelete(id: string){
    try{
      await api.delete(`/categories/${id}`)
      const allCategories = categories.filter((catalog) => catalog.uuid !== id)
      setCategories(allCategories)
    }catch(err){
      console.log(err)
    }
  }
    return (
      <>
        <h1 className="text-4xl font-medium text-white mb-7">Despesas</h1>
        {isForm && (
          <FormCategories setCategories={setCategories}/>
        )}
        <section className="flex flex-col gap-4" >
          {categories.map((category)  => (
          <article className="w-full bg-white rounded p-2 relative hover:scale-105 duration-200 z-0" key={category.uuid}>
          <p><span className="font-medium">None: </span>{category.name}</p>
          <p><span className="font-medium">Status: </span> 
          { category.is_active ? "ATIVO" : "INATIVO"}</p>
          <button className='bg-red-500 w-7 h-7 flex items-center justify-center rounded-lg absolute right-0 -top-2' onClick={() => handleDelete(category.uuid)}>
          <FiTrash size={18} color="#FFF"/>
          </button>
          </article>
          ))}
        </section>
      </>
    )
}
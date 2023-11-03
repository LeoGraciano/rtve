import { FormEvent, useEffect, useRef, useState } from 'react';
import { CategoriesProps, FormExpenditureProps } from '../entity/interfaces';
import { api, getCategories } from '../services/apis';


export default function FormExpenditure({ setExpenditure }: FormExpenditureProps) {
  const [categories, setCategories] = useState<CategoriesProps[]>([])
  const descriptionRef = useRef<HTMLInputElement | null>(null)
  const valueRef = useRef<HTMLInputElement | null>(null)
  const dateRef = useRef<HTMLInputElement | null>(null)
  const categoriesRef = useRef<HTMLSelectElement>(null)

  useEffect(() => {
    loadCategories()
  }, [])

  async function loadCategories() {
    setCategories(await getCategories())
  }

  async function handleSubmit(event: FormEvent){
    event.preventDefault()
    if (
      !descriptionRef.current?.value ||
      !valueRef.current?.value ||
      !dateRef.current?.value ||
      categoriesRef.current?.selectedOptions.length == 0
      ) {
        return;
      }

    const selectedOptions = Array.from(categoriesRef.current?.selectedOptions ?? []).map((option) => option.value);

    const response = await api.post("/expenditure/", {
      description: descriptionRef.current?.value,
      value: valueRef.current?.value,
      date: dateRef.current?.value,
      categories: selectedOptions,
    }
    )

    setExpenditure(allExpenditure=> [...allExpenditure, response.data])

    descriptionRef.current.value = ""
    valueRef.current.value = ""
    dateRef.current.value = ""
  }

    return (
        <form className="flex flex-col my-6 mb-8" onSubmit={handleSubmit}>
          <label className="font-medium text-white">Descrição:</label>
          <input type="text"
            name="description" id="id_description"
            placeholder="Descrição da despesa..."
            className="w-full mb-5 p-2 rounded"
            ref={descriptionRef}
          />
          <label className="font-medium text-white">Valor:</label>
          <input type="number"
            name="value" id="id_value"
            placeholder="Valor da despesa..."
            className="w-full mb-5 p-2 rounded"
            ref={valueRef}
          />
          <label className="font-medium text-white">Data:</label>
          <input type="date"
          name="date" id="id_date"
          placeholder="DD/MM/AAAA"
          className="w-full mb-5 p-2 rounded"
          ref={dateRef}
          />
          <label className="font-medium text-white">Categoria:</label>
          <select name="categories" id="id_categories" className="w-full mb-5 p-2 rounded" ref={categoriesRef} multiple>
            {categories.map((category) => (
              <option value={category.uuid} key={category.uuid}>{category.name}</option>
            ))}
          </select>
          <input type="submit" value="Registar" className="cursor-pointer w-full p-2 bg-green-500 rounded font-medium"/>
        </form>
    )
}
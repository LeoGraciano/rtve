import { useEffect, useState } from 'react';
import { FiEdit2, FiTrash } from 'react-icons/fi';
import { ExpenditureProps, ListExpenditureProps } from '../entity/interfaces';
import { api, getExpenditure } from '../services/apis';
import FormExpenditure from './FormExpenditure';


export default function ListExpenditure({ isForm }: ListExpenditureProps) {
  const [expenditure, setExpenditure] = useState<ExpenditureProps[]>([])


  useEffect(() => {
    loadExpenditure()
  }, [])

  async function loadExpenditure() {
    setExpenditure(await getExpenditure())
  }

  async function handleEdit(id: string){
    try{
      const response = await api.patch(`/expenditure/${id}/`)
      console.log(response.data)
    }catch(err){
      console.log(err)
    }
  }
  async function handleDelete(id: string){
    try{
      await api.delete(`/expenditure/${id}`)
      const allExpenditure = expenditure.filter((expense: any) => expense.uuid !== id)
      setExpenditure(allExpenditure)
    }catch(err){
      console.log(err)
    }
  }
    return (
      <>
        <h1 className="text-4xl font-medium text-white mb-7">Despesas</h1>
        {isForm && (
          <FormExpenditure setExpenditure={setExpenditure} />
        )}
        <section className="flex flex-col gap-4" >
          {expenditure.map((expense)  => (
          <article className="w-full bg-white rounded p-2 relative hover:scale-105 duration-200 z-0" key={expense.uuid}>
          <p><span className="font-medium">Despesa: </span>{expense.description}</p>
          <p><span className="font-medium">Valor: </span> R$ {expense.value}</p>
          <p><span className="font-medium">Data: </span> {expense.date}</p>
          <p><span className="font-medium">Categoria: </span> {expense.categories_display}</p>
          <p><span className="font-medium">Status: </span> 
          { expense.is_active ? "ATIVO" : "INATIVO"}</p>
          <button className='bg-red-500 w-7 h-7 flex items-center justify-center rounded-lg absolute right-0 -top-2' onClick={() => handleDelete(expense.uuid)}>
          <FiTrash size={18} color="#FFF"/>
          </button>
          <button onClick={() => handleEdit(expense.uuid)} className='bg-blue-500 w-7 h-7 flex items-center justify-center rounded-lg absolute right-7 -top-2'><FiEdit2 size={18} color="#FFF"/></button>

          </article>
          ))}
        </section>
      </>
    )
}
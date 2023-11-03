
export interface FormExpenditureProps {
    setExpenditure: React.Dispatch<React.SetStateAction<ExpenditureProps[]>>;
}
export interface FormCategoriesProps {
    setCategories: React.Dispatch<React.SetStateAction<CategoriesProps[]>>;
}

export interface ListExpenditureProps {
    isForm: boolean; // Defina o tipo de 'isForm' conforme necessário
}

export interface ListCategoriesProps {
    isForm: boolean; // Defina o tipo de 'isForm' conforme necessário
}


export interface ExpenditureProps{
    uuid: string;
    description: string;
    date: string;
    value: string;
    categories: string[];
    categories_display: string[];
    created_by: string;
    is_active: boolean;
}

export interface CategoriesProps{
    uuid: string;
    name: string; 
    is_active: boolean;
}

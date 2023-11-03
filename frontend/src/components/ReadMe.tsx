import { marked } from 'marked';
import { useEffect, useState } from 'react';

export default function ReadMe() {
  const [readmeContent, setReadmeContent] = useState('');

  useEffect(() => {
    const fetchReadme = async () => {
      try {
        const response = await fetch('/README.md');
        const text = await response.text();
        setReadmeContent(marked(text));
      } catch (error) {
        console.error('Erro ao buscar o arquivo README.md', error);
      }
    };

    fetchReadme();
  }, []);

  return (
    <div dangerouslySetInnerHTML={{ __html: readmeContent }} className='text-white'/>
  );
}

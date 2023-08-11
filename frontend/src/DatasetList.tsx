import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Dataset {
  id: string;
  name: string;
}

const DatasetList: React.FC = () => {
  const [datasets, setDatasets] = useState<Dataset[]>([]);

  axios.get('/v1/datasets/')
  .then(response => {
    setDatasets(response.data);
  })
  .catch(error => {
    console.error("There was an error fetching data:", error);
  });

  return (
    <div>
      <h2>Datasets</h2>
      <ul>
        {datasets.map((dataset) => (
          <li key={dataset.id}>{dataset.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default DatasetList;



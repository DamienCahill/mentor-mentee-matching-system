import { html } from 'htm/preact';
import { useEffect, useState } from 'preact/hooks';

const PublicProfileCategory = (props) => {
  const [selectedCategories, setSelectedCategories] = useState([]);
  useEffect(() => {
    fetchCategories();
  }, []);

  async function fetchCategories() {
    let selectedCategories = [];
    const mentorCategoriesRes = await fetch( `${props.apiUrl}/${props.mentorId}`, {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Accept': 'application/json',
      }
    });

    if( mentorCategoriesRes.ok ) {
      console.log('json');
      const json = await mentorCategoriesRes.json();
      setSelectedCategories(json);
      selectedCategories = json;
    }

  }
return html`
  <div class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">Selected Categories</h5>
        ${selectedCategories.map((categories, index) => (
          html`
            <a style="margin:3px;" class="btn btn-success" href="#">
              ${categories[1]} <i id=${categories[0]} name="${categories[1]}"></i>
            </a>
          `
        ))}
    </div>
  </div>
`;

};
export { PublicProfileCategory };
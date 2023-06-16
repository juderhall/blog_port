import { createClient } from '@sanity/client'
const client = createClient({
    projectId: 'bnpx4knh',
    apiVersion: '2023-06-15',
    dataset: 'production',
    token: 'skNP4wJzEwq2kDBcybVZdLGDA03R9AZ1ISXDtgVFcHDi2NkMdubu8WUdRkxa9WUWnQFRK3ocGqIFPQyaelUk8fJnYrKAkMNuT3oSw5cxMVKVTQHLaEHg9P3Ot7ibhaeViNvYDsWXmU10gmPzPmrhJz7rHZsD915PiJqnNcN4gMqftAo6i85V',
    useCdn: false
})

const currentDateISO = new Date().toISOString()

/*
Sample GROQ query to get post we are about to create
(You can view this in Sanity's Vision tab)

*[_type == "post" && title == "My first post"]{
    ...,
}

*/

//TODO: Hero image w/ caption and alt tags, author, categories


client.create({
    //Need an image
    slug: {
        current: 'my-first-post', //We need to push the slug here
        _type: 'slug'
    },
    _type: 'post',
    title: 'My first post',
    excerpt: 'This is coming from the API',
    _createdAt: currentDateISO,
    _updatedAt: currentDateISO,
    mainImage: {
        _type: 'image',
        alt: "We need to collect the alt tag", //Alt tag goes here
        caption: "We need to collect the caption", //Caption goes here
        asset: {
            _ref: "image-131f58078c3dab09175c2f452391bde7cd4c1e12-530x530-png", //Need to mass upload then collect the image reference
            _type: "reference"
        }
    },
    //Body is where all of the content goes
    body: [
        {
            _type: 'block',
            style: 'normal',
            markDefs: [],
            children: [
                {
                    _type: 'span',
                    text: 'This blog is being pushed over from an API, it is not being created in the Sanity Studio.'
                }
            ]
            //Needs a key
        }
    ]
})
.then(res => {
    console.log(`document was created, document ID is ${res._id}`)
}).catch(err => {
    console.error('Oh no, the update failed: ', err.message)
})
import { createClient } from '@sanity/client'
const client = createClient({
    projectId: 'bnpx4knh',
    apiVersion: '2023-06-15',
    dataset: 'production',
    token: 'skNP4wJzEwq2kDBcybVZdLGDA03R9AZ1ISXDtgVFcHDi2NkMdubu8WUdRkxa9WUWnQFRK3ocGqIFPQyaelUk8fJnYrKAkMNuT3oSw5cxMVKVTQHLaEHg9P3Ot7ibhaeViNvYDsWXmU10gmPzPmrhJz7rHZsD915PiJqnNcN4gMqftAo6i85V',
    useCdn: false
})


/*
*[_type == "post" && title == "My first post"]{
    ...,
}

*/
//globalKey should be incremented by 1 for each new block

const currentDateISO = new Date().toISOString()
let BlockTypes = [
    'normal',
    'h1',
    'h2',
    'h3',
    'h4',
]
const Headers = (text, globalKey=0) => {
    return {
        _type: 'block',
        style: 'h2',
        markDefs: [], //This may hold styles
        children: [
            {
                text: text,
                _key: `h2-${globalKey+1}`,
                _type: 'span',
                marks: [] //Wonder what this is for
            },
        ],
        _key: `h2-${globalKey+2}`,
    }
}

//TODO: Hero image w/ caption and alt tags, author, categories

client.create({
    //Need an image
    _type: 'post',
    slug: {
        current: 'my-first-post', //We need to push the slug here
        _type: 'slug'
    },
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
        },
        {
            style: 'h3',
            children: [
                {
                    text: 'HELLO!'
                }
            ]
        }
    ]
})
.then(res => {
    console.log(`document was created, document ID is ${res._id}`)
}).catch(err => {
    console.error('Oh no, the update failed: ', err.message)
})